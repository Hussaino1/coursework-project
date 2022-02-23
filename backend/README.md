# Backend API

- [Backend API](#backend-api)
  - [Summary](#summary)
  - [`GET`](#get)
    - [`/read/allCourseworks`](#readallcourseworks)
    - [`/read/coursework/{id}`](#readcourseworkid)
  - [`POST`](#post)
    - [`/create/coursework`](#createcoursework)
  - [`PUT`](#put)
    - [`/update/coursework/{id}`](#updatecourseworkid)
    - [`/finish/coursework/{id}`](#finishcourseworkid)
    - [`/unfinished/coursework/{id}`](#unfinishedcourseworkid)
  - [`DELETE`](#delete)
    - [`/delete/coursework/{id}`](#deletecourseworkid)

## Summary

| URL                     | Method   | Request Body               |
| ----------------------- | -------- | -------------------------- |
| `/read/allCourseworks`        | `GET`    | None                       |
| `/read/coursework/{id}`       | `GET`    | None                       |
| `/create/coursework`          | `POST`   | `{"brief": <value>}` |
| `/update/coursework/{id}`     | `PUT`    | `{"brief": <value>}` |
| `/finish/coursework/{id}`   | `PUT`    | None                       |
| `/unfinished/coursework/{id}` | `PUT`    | None                       |
| `/delete/coursework/{id}`     | `DELETE` | None                       |

## `GET`

### `/read/allCourseworks`

Example Response

```json
{
    "courseworks": [
        {
            "id": 1,
            "brief": "Work of Shakespeare",
            "finishd": "true"
        },
        {
            "id": 2,
            "brief": "American West",
            "finishd": "false"
        }
    ]
}
```

### `/read/coursework/{id}`

Path Parameters

| Parameter | Brief                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the coursework to query from the database |

Example Response

```json
{
    "id": 1,
    "brief": "Work of Shakespeare",
    "finishd": "true"
}
```

## `POST`

### `/create/coursework`

Example Request

```json
{
    "brief": "Work of Shakespeare"
}
```

Example Response

```text
Added coursework with brief: Work of Shakespeare
```

## `PUT`

### `/update/coursework/{id}`

Path Parameters

| Parameter | Brief                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the coursework to query from the database |

Example Request

```json
{
    "brief": "American West"
}
```

Example Response

```text
Updated coursework (ID: 1) with brief: Work of shakespeare
```

### `/finish/coursework/{id}`

Path Parameters

| Parameter | Brief                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the coursework to query from the database |

Example Response

```text
Coursework with ID: 1 set to finishd = False
```

### `/unfinished/coursework/{id}`

Path Parameters

| Parameter | Brief                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the coursework to query from the database |

Example Response

```text
Coursework with ID: 1 set to finishd = True
```

## `DELETE`

### `/delete/coursework/{id}`

Path Parameters

| Parameter | Brief                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the coursework to query from the database |

Example Response

```text
Deleted coursework with ID: 1
```
