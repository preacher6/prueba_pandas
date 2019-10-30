from bokeh.plotting import figure
from bokeh.io import output_file, show

x = list(range(1, 6))
y = [6, 7, 2, 4, 5]
p = figure(title='simple line example',
        x_axis_label='x',
        y_axis_label='y')
p.line(x, y, legend='Temp.', line_width=2)
output_file('lines.html')
show(p)