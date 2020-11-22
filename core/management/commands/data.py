from django.core.management.base import BaseCommand, CommandError
from core.models import *
from core.serializers import *
from django.utils.dateparse import parse_date
patients = [
    {
        "ohip_id": "0000-000-000-AA",
        "name": "John Doe",
        "dob": "2000-01-01",
        "gender": "male",
        "address": "123 Sesame Street, Toronto, ON M5V 3L9",
        "clinic_id": 33070,
    },
    {
        "ohip_id": "3695-420-235-PQ",
        "name": "Daniel C. Rose",
        "dob": "1950-03-21",
        "gender": "male",
        "address": "3513 Derry Road, Malton, ON L4T 1A8",
        "clinic_id": 10001,
    },
    {
        "ohip_id": "8734-489-567-BS",
        "name": "Arlene T. Haywood",
        "dob": "1972-08-12",
        "gender": "female",
        "address": "1942 Woodvale Drive, Dutton, ON N0L 1J0",
        "clinic_id": 33070,
    },
    {
        "ohip_id": "1299-630-187-AK",
        "name": "Kathryn M. Connelly",
        "dob": "1964-06-19",
        "gender": "female",
        "address": "2056 Barton Street, Hamilton, ON L8P 1P8",
        "clinic_id": 22101,
    },
    {
        "ohip_id": "2208-001-209-MS",
        "name": "Nicolas J. Eoff",
        "dob": "1953-11-20",
        "gender": "male",
        "address": "1394 Algonquin Blvd, Timmins, ON P4N 1C3",
        "clinic_id": 10001,
    }
]
doctors = [
    {
        "cpso_id": 107896,
        "name": "Dr. Gregory House, M.D.",
        "gender" : "male",
        "specialty": "nephrology",
        "clinic_id": 10001,
    },
    {
        "cpso_id": 564378,
        "name": "Dr. Janet Wilson, M.D.",
        "gender": "female",
        "specialty": "family medicine",
        "clinic_id": 10001,
    },
    {
        "cpso_id": 100013,
        "name":"Dr. Remy Hadley, M.D.",
        "gender": "female",
        "specialty": "pediatrics",
        "clinic_id": 33070,

    },
    {
        "cpso_id": 420169,
        "name": "Dr. Michael Taub, M.D.",
        "gender":"male",
        "specialty": "family medicine",
        "clinic_id": 33070
    },
    {
        "cpso_id": 246710,
        "name":"Dr. Charlotte Webb, M.D.",
        "gender": "female",
        "specialty": "cardiology",
        "clinic_id": 22101,
    }
]
clinics = [
    {
        "clinic_id": 10001,
        "name": "Downtown Doctors Walk In Medical Clinic",
        "days": "monday",
        "address": "181 Bay St 30th Floor, Toronto, ON M5J 2T3",
    },
    {
        "clinic_id": 33070,
        "name": "Queen Spadina Medical Centre",
        "days": "tuesday",
        "address": "455 Queen St W, Toronto, ON M5V 2A9"
    },
    {
        "clinic_id": 22101,
        "name": "Centretown Community Health Centre",
        "days": "wednesday",
        "address": "420 Cooper St, Ottawa, ON K2P 2N6"
    }
]
appointments = [
    {
        "clinic_id": 10001,
        "ohip_id": "3695-420-235-PQ",
        "cpso_id": 564378,
        "appointment_type": "full checkup",
        "start_time": "10:00 a.m.",
        "end_time": "10:30 a.m.",
        "date": "2020-11-21",
        "duration": 30,
        "address": "181 Bay St 30th Floor, Toronto, ON M5J 2T3",
    },
    {
        "clinic_id": 10001,
        "ohip_id": "2208-001-209-MS",
        "cpso_id": 107896,
        "appointment_type": "prescription refill",
        "start_time": "11:00 a.m.",
        "end_time": "11:10 a.m.",
        "date": "2020-11-21",
        "duration": 10,
        "address": "181 Bay St 30th Floor, Toronto, ON M5J 2T3",
    },
    {
        "clinic_id": 33070,
        "ohip_id": "8734-489-567-BS",
        "cpso_id": 100013,
        "appointment_type": "vitals checkup",
        "start_time": "12:00 p.m.",
        "end_time": "12:15 p.m.",
        "date": "2020-11-19",
        "duration": 15,
        "address": "455 Queen St W, Toronto, ON M5V 2A9"
    },
    {
        "clinic_id": 33070,
        "ohip_id": "0000-000-000-AA",
        "cpso_id": 420169,
        "appointment_type": "general consultation",
        "start_time": "1:00 p.m.",
        "end_time": "1:30 p.m.",
        "date": "2020-11-19",
        "duration": 30,
        "address": "455 Queen St W, Toronto, ON M5V 2A9"
    },
    {
        "clinic_id": 22101,
        "ohip_id": "1299-630-187-AK",
        "cpso_id": 246710,
        "appointment_type": "vaccination",
        "start_time": "4:15 p.m.",
        "end_time": "4:25 p.m.",
        "date": "2020-11-19",
        "duration": 10,
        "address": "420 Cooper St, Ottawa, ON K2P 2N6"
    }
]


class Command(BaseCommand):
    help = 'create/delete sample data'
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='create/delete sample data')

    def handle(self, *args, **options):
        if options['command']== 'create':
            serializer = ClinicSerializer(None, data=clinics, many=True)
            if serializer.is_valid():
                serializer.save()
            self.stdout.write(self.style.SUCCESS(str(serializer.errors)))
            serializer = PatientSerializer(None,data=patients, many=True)
            if serializer.is_valid():
                serializer.save()
            self.stdout.write(self.style.SUCCESS(str(serializer.errors)))
            serializer = DoctorSerializer(None,data=doctors, many=True)
            if serializer.is_valid():
                serializer.save()
            self.stdout.write(self.style.SUCCESS(str(serializer.errors)))
            serializer = AppointmentSerializer(None,data=appointments, many=True)
            if serializer.is_valid():
                serializer.save()
            self.stdout.write(self.style.SUCCESS(str(serializer.errors)))
            self.stdout.write(self.style.SUCCESS('Successfully created data'))
        elif options["command"] ==  "delete":
            try:
                Patient.objects.all().delete()
                Doctor.objects.all().delete()
                Clinic.objects.all().delete()
                Appointment.objects.all().delete()
            except:
                raise CommandError('failure in deleting sample data')
            self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
        else:
            raise CommandError("not a valid command")
                

