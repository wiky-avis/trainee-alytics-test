from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure


def graph_create(points, title, xlabel, ylabel):
    fig = Figure(facecolor = 'white', edgecolor = 'white')
    graph = fig.add_subplot(111)

    graph.set_title(title)
    graph.set_xlabel(xlabel)
    graph.set_ylabel(ylabel)

    graph.grid()

    for x, y, f in points:
        graph.plot_date(x, y, f)

    graph.xaxis.set_major_formatter(DateFormatter("%Y.%m.%d %H:%M"))
    fig.autofmt_xdate()
    output = BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(output)
    data = output.getvalue()
    return data


def get_graph():
    x, y = [1, 2, 3], [2, 3, 4]
    u, v = [-1, -2, -3], [-2, -3, -5]
    title = u'Пробный график'
    xlabel = u'Время'
    ylabel = u'Энергия'
    points = [(x, y, 'g^'), (u, v, 'ro')]
    graph = graph_create(points, title, xlabel, ylabel)
    img = SimpleUploadedFile(
        name='media/graphs/graph.png',
        content=graph,
        content_type='image/png'
        )
    return img
