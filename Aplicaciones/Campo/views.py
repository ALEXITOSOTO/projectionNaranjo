from django.shortcuts import render
from Aplicaciones.Gestion.models import Area, Responsable, Bloques, Variedades
from .models import ConteoDiario
from django.db.models import Sum, Case, When, IntegerField
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse


def registro_diario(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        dia = request.POST.get('dia')
        conteo_del_dia = request.POST.get('conteo_del_dia')
        area_id = request.POST.get('area')
        responsable_id = request.POST.get('responsable')
        bloque_id = request.POST.get('bloque')
        variedad_id = request.POST.get('variedad')

        area = Area.objects.get(id=area_id)
        responsable = Responsable.objects.get(id=responsable_id)
        bloque = Bloques.objects.get(id=bloque_id)
        variedad = Variedades.objects.get(id=variedad_id)

        ConteoDiario.objects.create(
            fecha=fecha,
            dia=dia,
            conteo_del_dia=conteo_del_dia,
            area=area,
            responsable=responsable,
            bloque=bloque,
            variedad=variedad
        )

        # Añadir mensaje de éxito
        context = {
            'areas': Area.objects.all(),
            'responsables': Responsable.objects.all(),
            'bloques': Bloques.objects.all(),
            'variedades': Variedades.objects.all(),
            'success_message': 'Registro guardado exitosamente.',
        }
        return render(request, 'Conteo/diario.html', context)

    # Si no es POST, se carga el formulario vacío
    context = {
        'areas': Area.objects.all(),
        'responsables': Responsable.objects.all(),
        'bloques': Bloques.objects.all(),
        'variedades': Variedades.objects.all(),
    }
    return render(request, 'Conteo/diario.html', context)

def diario(request):
    conteos_diarios = ConteoDiario.objects.all()
    context = {
        'conteos_diarios': conteos_diarios,
    }
    return render(request, 'Ingreso/diario.html', context)

def mostrar_conteos(request):
    conteos_diarios = ConteoDiario.objects.all()

    # Agregaciones por día
    total_semanal_dia = conteos_diarios.values('dia').annotate(
        total=Sum('conteo_del_dia')
    ).order_by('dia').aggregate(
        Lunes=Sum(Case(When(dia="Lunes", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        Martes=Sum(Case(When(dia="Martes", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        Miércoles=Sum(Case(When(dia="Miércoles", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        Jueves=Sum(Case(When(dia="Jueves", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        Viernes=Sum(Case(When(dia="Viernes", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        Sábado=Sum(Case(When(dia="Sábado", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        Domingo=Sum(Case(When(dia="Domingo", then='conteo_del_dia'), default=0, output_field=IntegerField())),
        total_general=Sum('conteo_del_dia')
    )

    context = {
        'conteos_diarios': conteos_diarios,
        'total_semanal_dia': total_semanal_dia
    }
    return render(request, 'Ingreso/diario.html', context)


def generar_reporte(request):
    # Crear un objeto HttpResponse con el contenido tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_conteo.pdf"'

    # Crear el documento PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Obtener datos de ConteoDiario
    conteos_diarios = ConteoDiario.objects.all()
    
    # Preparar datos para la tabla
    data = [['Fecha', 'Día', 'Conteo del Día', 'Área', 'Responsable', 'Bloque', 'Variedad']]
    for conteo in conteos_diarios:
        data.append([
            conteo.fecha,
            conteo.dia,
            conteo.conteo_del_dia,
            conteo.area.nombre,  # Asumiendo que el modelo Area tiene un campo 'nombre'
            conteo.responsable.nombre,  # Asumiendo que el modelo Responsable tiene un campo 'nombre'
            conteo.bloque.nombre,  # Asumiendo que el modelo Bloques tiene un campo 'nombre'
            conteo.variedad.nombre  # Asumiendo que el modelo Variedades tiene un campo 'nombre'
        ])

    # Crear y estilizar la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)

    # Construir el documento
    doc.build(elements)

    return response