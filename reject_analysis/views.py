from django.shortcuts import render

from patients.models.Patient import Patient

from patients.models.AcquiredImageStatus import AcquiredImageStatus

from utils.matplotbase import get_plot

import matplotlib.pyplot as plt
import io
import base64
# Create your views here.

# def factor_exam_view(request):
#     data = YourModel.objects.all()
#     return render(request, 'tables/factor_exam.html', {'data': data})

def reject_accept_rate_view(request):
    total_items = float(AcquiredImageStatus.objects.count())
    total_reject = float(AcquiredImageStatus.objects.filter(image_status='Rejected').count())
    total_accept = float(AcquiredImageStatus.objects.filter(image_status='Accepted').count())
    if total_items != 0:
        reject_rate = (total_reject / total_items) * 100
        accept_rate = (total_accept / total_items) * 100
    else:
        reject_rate = 45.0
        accept_rate = 55.0
    data = [reject_rate, accept_rate]
    return render(request, 'tables/reject_accept_rate.html', {'data': data})

def analysis_view(request):
    query_selected = Patient.objects.all()
    x = [x.name for x in query_selected]
    y = [y.age for y in query_selected]
    chart = get_plot(x, y)
    return render(request, 'pages/reject_analysis.html', {'chart': chart})


def bar_chart_view(request):
    # Sample data
    categories = ['Category A', 'Category B', 'Category C']
    values = [25, 40, 30]

    # Create a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart Example')

    # Convert the plot to a BytesIO object and then to base64 for embedding in HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the plot_data to the template
    context = {'plot_data': plot_data}

    return render(request, 'charts/bar_chart.html', context)


def grouped_bar_chart_view(request):
    # Sample data
    categories = ['Category A', 'Category B', 'Category C']
    values1 = [25, 40, 30]
    values2 = [15, 30, 25]

    # Create a grouped bar chart
    x = range(len(categories))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x, values1, width, label='Group 1')
    plt.bar([i + width for i in x], values2, width, label='Group 2')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Grouped Bar Chart Example')
    plt.xticks([i + width / 2 for i in x], categories)
    plt.legend()

    # Convert the plot to a BytesIO object and then to base64 for embedding in HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the plot_data to the template
    context = {'plot_data': plot_data}

    return render(request, 'charts/grouped_bar_chart.html', context)

def grouped_bar_chart_view(request):
    # Sample data
    categories = ['Category A', 'Category B', 'Category C']
    values1 = [25, 40, 30]
    values2 = [15, 30, 25]

    # Create a grouped bar chart
    x = range(len(categories))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x, values1, width, label='Group 1')
    plt.bar([i + width for i in x], values2, width, label='Group 2')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Grouped Bar Chart Example')
    plt.xticks([i + width / 2 for i in x], categories)
    plt.legend()

    # Convert the plot to a BytesIO object and then to base64 for embedding in HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the plot_data to the template
    context = {'plot_data': plot_data}

    return render(request, 'charts/grouped_bar_chart.html', context)


def pie_chart_view(request):
    # Sample data
    labels = ['Label 1', 'Label 2', 'Label 3']
    sizes = [40, 30, 20]

    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Pie Chart Example')

    # Convert the plot to a BytesIO object and then to base64 for embedding in HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the plot_data to the template
    context = {'plot_data': plot_data}

    return render(request, 'charts/pie_chart.html', context)
