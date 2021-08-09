"""Tests for the qtpdf preprocessor"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from .base import ExportersTestsBase
from ..qtpdf import QtPDFExporter

class TestQtPDFExporter(ExportersTestsBase):
    """Contains test functions for qtpdf.py"""

    exporter_class = QtPDFExporter

    def test_export(self):
        """
        Can a TemplateExporter export something?
        """
        (output, resources) = QtPDFExporter().from_filename(self._get_notebook())
        assert len(output) > 0