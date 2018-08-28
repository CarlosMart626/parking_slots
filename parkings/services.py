from django.conf import settings

class AssingParkingLotService:
    def __init__(self, users):
        self.users = users
        self.validate_users()
    
    def validate_users(self):
        for user in self.users:
            assert 'distance' in user.keys(), "'distance' not found"
            assert 'name' in user.keys(), "'name' not found"
            assert 'work_days' in user.keys(), "'work_days' not found"
            assert len(user.get('work_days')) > 0, "'work_days' wrong length"
            for work_day in user.get('work_days'):
                assert work_day in settings.AVAILABLE_PARKING_DAYS, f"Not a valid day: '{work_day}''"

    def get_priority(self, d):
        """ Return the value of a key in a dictionary. """
        return d["priority"]

    def get_user_priority(self, user):
        priority = user['distance'] * 10
        priority = priority / len(user['work_days'])
        return priority

    def get_day(self, day=None):
        day_user_list = []
        for user in self.users:
            if day in user['work_days']:
                user_dict = {
                    'name': user['name'],
                    'priority': self.get_user_priority(user)
                }
                day_user_list.append(user_dict)
        selected_ones = sorted(day_user_list, key=self.get_priority, reverse=True)[:settings.AVAILABLE_PARKING_LOTS]
        return [user.get('name') for user in selected_ones]

    def get_week_schedule(self):
        days = settings.AVAILABLE_PARKING_DAYS
        result = []
        for day in days:
            result_day = {
                'day': day,
                'assigned': self.get_day(day)
            }
            result.append(result_day)
        return result
