# Parking slots project
This Django project is intented to priorityze the parking lots. This project runs using docker and has a REST API with one endpoint.

## Settings
In `settings.py` you can define:

### AVAILABLE_PARKING_LOTS
This settings will let you define the number of parking slots available
```
AVAILABLE_PARKING_LOTS = 4
```

### AVAILABLE_PARKING_DAYS
This settings will let you define the week days of availability of parking slots by default is the whole week
```
AVAILABLE_PARKING_DAYS = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
]
```
Note: This list is going to be use to validate the input structure to get the parking lot schedule so you can define your own.

## Running
`docker-compose up` the api will be running at `http://localhost:9000/`

## Getting the schedule
### User structure
```json
{   
    "name": "user1",
    "distance": 8,
    "work_days": [
        "tuesday",
        "wednesday",
        "thursday"
    ]
}
```
### Example
#### Request
```json
POST "http://localhost:9000/parking/"
payload = [
    {   
        "name": "user1",
        "distance": 8,
        "work_days": [
            "tuesday",
            "wednesday",
            "thursday"
        ]
    },
    {   
        "name": "user2",
        "distance": 30,
        "work_days": [
            "monday",
            "tuesday",
            "wednesday",
            "thursday"
        ]
    },
    {   
        "name": "user3",
        "distance": 5,
        "work_days": [
            "monday",
            "tuesday",
            "wednesday"
        ]
    }
]
```
#### Response
```json
[
    {
        "day": "monday",    <--- day of week
        "assigned": [       <--- assigned users
            "user2",        <--- username
            "user3"         <--- username
        ]
    },
    {
        "day": "tuesday",
        "assigned": [
            "user2",
            "user1",
            "user3"
        ]
    },
    {
        "day": "wednesday",
        "assigned": [
            "user2",
            "user1",
            "user3"
        ]
    },
    {
        "day": "thursday",
        "assigned": [
            "user2",
            "user1"
        ]
    },
    {
        "day": "friday",
        "assigned": []
    }
]
```
