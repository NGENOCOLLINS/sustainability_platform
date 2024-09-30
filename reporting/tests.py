from django.test import TestCase
from .models import SustainabilityReport

class SustainabilityReportModelTest(TestCase):
    def test_report_creation(self):
        report = SustainabilityReport.objects.create(
            title='Test Report',
            description='Test description'
        )
        self.assertEqual(report.title, 'Test Report')
