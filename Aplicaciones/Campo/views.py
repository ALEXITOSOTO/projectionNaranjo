from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from Aplicaciones.Gestion.models import Area, Responsable, Bloques, Variedades
from .models import ConteoDiario
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os
from django.db.models import Sum, F, FloatField, ExpressionWrapper

def conteo_diario(request):
    context = {
        'areas': Area.objects.all(),
        'responsables': Responsable.objects.all(),
        'bloques': Bloques.objects.all(),
        'variedades': Variedades.objects.all(),
    }
    return render(request, "Conteo/diario.html", context)

def conteo_diario_view(request):
    conteos_diarios = ConteoDiario.objects.select_related('area', 'bloque', 'responsable', 'variedad').all()
    total_camas_contadas = 0
    total_plantas_por_cama = 0
    total_resultado = 0
    total_nacional = 0
    total_exportable = 0
    for conteo in conteos_diarios:
        if conteo.camas > 0:
            resultado = (conteo.plantas_por_cama / conteo.camas) * conteo.bloque.numero_camas
        else:
            resultado = 0
        
        nacional = resultado * 0.08
        exportable = resultado * 0.92
        total_camas_contadas += conteo.camas
        total_plantas_por_cama += conteo.plantas_por_cama
        total_resultado += resultado
        total_nacional += nacional
        total_exportable += exportable
    context = {
        'conteos_diarios': conteos_diarios,
        'total_camas_contadas': total_camas_contadas,
        'total_plantas_por_cama': total_plantas_por_cama,
        'total_resultado': total_resultado,
        'total_nacional': total_nacional,
        'total_exportable': total_exportable,
    }
    
    return render(request, 'Ingreso/diario.html', context)



def obtener_camas_bloque(request):
    bloque_id = request.GET.get('bloque_id')
    print(f"ID del bloque recibido: {bloque_id}") 
    try:
        bloque = Bloques.objects.get(id=bloque_id)
        print(f"Número de camas en el bloque: {bloque.numero_camas}")
        data = {
            'numero_camas': bloque.numero_camas
        }
    except Bloques.DoesNotExist:
        data = {
            'error': 'Bloque no encontrado'
        }
    return JsonResponse(data)







def generar_reporte(request):
    # Crear un objeto HttpResponse con el contenido tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_conteo.pdf"'

    # Crear el documento PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Estilos para el PDF
    styles = getSampleStyleSheet()
    
    # Agregar un título
    title = Paragraph("Reporte Diario de Conteo", styles['Title'])
    elements.append(title)

    # Ruta de la imagen en static
    image_path = '/home/belagd/Documents/Proyectos/projectionnaranjo/projectionNaranjo/static/plantilla/BLK/assets/img/logoN.png'

    # Agregar la imagen
    logo = Image(image_path)
    logo.width = 200  # Ajusta el tamaño según sea necesario
    logo.height = 100
    logo.hAlign = 'CENTER'
    elements.append(logo)

    # Obtener datos de ConteoDiario
    conteos_diarios = ConteoDiario.objects.all()
    
    # Preparar datos para la tabla
    data = [['Fecha', 'Día', 'Conteo del Día', 'Área', 'Responsable', 'Bloque', 'Variedad']]
    for conteo in conteos_diarios:
        data.append([
            conteo.fecha,
            conteo.dia,
            conteo.conteo_del_dia,
            conteo.area.nombre,
            conteo.responsable.nombre,
            conteo.bloque.nombre,
            conteo.variedad.nombre
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

    # Agregar un pie de página
    footer = Paragraph("Reporte generado el: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), styles['Normal'])
    elements.append(footer)

    # Construir el documento
    doc.build(elements)

    return response