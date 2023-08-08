from django.test import TestCase
from logs.models import Log


class LogModelTestCase(TestCase):
    def setUp(self):
        Log.objects.create(description="Test log entry",
                           duration=60, date="2023-08-05")

    def test_create_log(self):
        # Create a new Log instance
        log_entry = Log.objects.create(
            description="New log entry",
            duration=120,
            date="2023-08-06"
        )

        # Retrieve the created Log instance from the database
        created_log = Log.objects.get(description="New log entry")

        # Verify attributes of the created Log instance
        self.assertEqual(created_log.description, "New log entry")
        self.assertEqual(created_log.duration, 120)
        self.assertEqual(created_log.date.strftime('%Y-%m-%d'), "2023-08-06")

    def test_model_str(self):
        log_entry = Log.objects.get(description="Test log entry")
        expected_str = f"{log_entry.description} - {log_entry.date}"
        self.assertEqual(str(log_entry), expected_str)

    def test_duration_positive(self):
        log_entry = Log.objects.get(description="Test log entry")
        self.assertGreaterEqual(log_entry.duration, 0)

    def test_date_auto_now_add(self):
        log_entry = Log.objects.get(description="Test log entry")
        self.assertIsNotNone(log_entry.date)

    def test_date_format(self):
        log_entry = Log.objects.get(description="Test log entry")
        self.assertEqual(log_entry.date.strftime('%Y-%m-%d'), "2023-08-05")
