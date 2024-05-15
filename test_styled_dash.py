import dash
from dash import html, dcc
from dash.testing import wait
import pytest

from styled_dash import app

@pytest.fixture
def client():
    return app.server


def test_header_present(client):
    # Access the app layout
    layout = app.layout
    # Check if the header is present
    assert isinstance(layout, html.Div)
    assert any(isinstance(child, html.H1) and child.children == "Sales Visualizer" for child in layout.children)


def test_visualization_present(client):
    # Access the app layout
    layout = app.layout
    # Check if the visualization component is present
    assert any(isinstance(child, dcc.Graph) and child.id == "sales-chart" for child in layout.children)


def test_region_picker_present(client):
    # Access the app layout
    layout = app.layout
    # Check if the region picker component is present within the expected parent element (html.Div)
    assert any(isinstance(child, html.Div) and
               any(isinstance(grandchild, dcc.RadioItems) and grandchild.id == "region-filter" for grandchild in child.children)
               for child in layout.children)


if __name__ == "__main__":
    pytest.main(['-vv'])
