import matplotlib.pyplot as plt
import base64

from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    # switching the backend
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Patient ages')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('name')
    plt.ylabel('age')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_bar_chart(categories, values, cat_name, val_name, chart_title, fig_width, fig_height):
    # Create a bar chart
    plt.figure(figsize=(fig_width, fig_height))
    plt.bar(categories, values)
    plt.xlabel(cat_name)
    plt.ylabel(val_name)
    plt.title(chart_title)
    # Convert the plot to a BytesIO object and then to base64 for embedding in HTML
    plot_data = get_graph()
    return plot_data

def get_pie_chart(labels, sizes, fig_width, fig_height, fig_title):
    # Create a pie chart
    plt.figure(figsize=(fig_width, fig_height))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(fig_title)
    plot_data = get_graph()

    return plot_data

# def grouped_bar_chart_view(categories, cat_name, val_name, chart_title, fig_width, fig_height, values1, values2, values3):
#     # Sample data
#     categories = ['Category A', 'Category B', 'Category C']
#     values1 = [25, 40, 30]
#     values2 = [15, 30, 25]
#
#     # Create a grouped bar chart
#     x = range(len(categories))
#     width = 0.35
#
#     plt.figure(figsize=(fig_width, fig_height))
#     plt.bar(x, values1, width, label='Group 1')
#     plt.bar([i + width for i in x], values2, width, label='Group 2')
#     plt.xlabel('Categories')
#     plt.ylabel('Values')
#     plt.title('Grouped Bar Chart Example')
#     plt.xticks([i + width / 2 for i in x], categories)
#     plt.legend()
#
#     # Convert the plot to a BytesIO object and then to base64 for embedding in HTML
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plot_data = base64.b64encode(buffer.read()).decode('utf-8')
#     buffer.close()
#
#     # Pass the plot_data to the template
#     context = {'plot_data': plot_data}
#
#     return render(request, 'charts/grouped_bar_chart.html', context)


