
# ScoreAPI

Sistema de calificaciones escolares usando Django Rest Framework.



## Referencia del API

#### Create User (Student)

```http
  POST /users/create
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. |
| `password` | `string` | **Required**. |


#### Create Teacher

```http
  POST teachers/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. |
| `password`      | `string` | **Required**. |

#### Create Course

**Permissions**: Can only be used by Teachers.
```http
  POST courses/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `course_name`      | `string` | **Required**. |
| `teacher`      | `int` | Automatically receives the id(PK) from the logged Teacher |

#### Create Assignment

**Permissions**: Can only be used by Teachers.
```http
  POST assignments/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `course`      | `int` | **Required**. PK of the course |
| `title`      | `string` | **Required** |

#### Send  Assignment

**Permissions**: Can only be used by Students.

```http
  POST studentAssignment/send/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `assignment`      | `int` | **Required**. PK of the assignment |
| `comment`      | `string` | **Optional** |
| `score`      | `int` | **Automatically set to NULL until graded**. Can't be changed by the student. |

#### Grade  Assignment

**Permissions**: Can only be used by Teachers.

```http
  PUT studentAssignment/grade/<int:pk>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `score`      | `int` | **Required** |




# Libraries 

scoreAPI uses:

- asgiref 3.5.2
- Django 4.0.4
- djangorestframework 3.13.1
- pytz 2022.1
- sqlparse 0.4.2
- tzdata 2022.1

It uses **SQLite** as database engine.

# Postman Collection

The collection is found in the Prueba Backend .postman_collection file.
