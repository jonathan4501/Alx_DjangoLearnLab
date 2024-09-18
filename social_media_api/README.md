# Follow Endpoints

## Follow a User

* **URL:** `/accounts/follow/<int:user_id>/`
* **Method:** `POST`
* **Description:** Follow a user.
* **Request Body:** None
* **Response:** `200 OK` if successful, `404 Not Found` if the user does not exist.

## Unfollow a User

* **URL:** `/accounts/unfollow/<int:user_id>/`
* **Method:** `POST`
* **Description:** Unfollow a user.
* **Request Body:** None
* **Response:** `200 OK` if successful, `404 Not Found` if the user does not exist.

# Feed Endpoint

## Get Feed

* **URL:** `/posts/feed/`
* **Method:** `GET`
* **Description:** Get the feed of posts from followed users.
* **Request Body:** None
* **Response:** A list of posts in JSON format, ordered by creation date.