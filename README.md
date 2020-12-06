# Backend REST shop-app


** Python / Django Rest Framework
** VueJS 2.6.11

** redis cache -> 1 day (search products)

### Deploy com Docker

    ./run.sh

-> ** get the token JWT**

    $ curl -i -H "Content-Type: application/json" \
        -X POST -d '{ "username": "admin", "password": "admin_pass" }' http://localhost/token/

-> **create client**

    $ curl -i -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" -X POST -d '{ "name": "joao do shopping", "email": "jose@shop.com" }' http://localhost/customers/

-> **get details client**

    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" http://localhost/customers/9af3de6c-8ea5-4c26-a3fd-03253afd50a5/


-> **update client**

    $ curl -i -H "Content-Type: application/json" \-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" -X PUT -d '{ "name": "joao do shopping Silva", "email": "jose@shop.com" }' http://localhost/customers/9af3de6c-8ea5-4c26-a3fd-03253afd50a5/


-> **remove client**

    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" -X DELETE http://localhost/customers/9af3de6c-8ea5-4c26-a3fd-03253afd50a5/


-> **get produt favorite**

    $ curl -i -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" -d '{ "product_id": "a96b5916-9109-5d2e-138a-7b656efe1f92", "customer": "d705e535-d31a-48b9-9bd7-c193053b5f82" }' -X POST http://localhost/favorites/


-> **get produts favorite the client**

    $ curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" http://localhost/customers/d705e535-d31a-48b9-9bd7-c193053b5f82/favorites/


-> **delete the produt favorite**

    curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1MDA5OTc0LCJqdGkiOiJlZDVlNWVjZjIyZDE0YTVmODcwNWRkZDE3NTkzZWJhMyIsInVzZXJfaWQiOjF9.RhrlIFn7EGdNiWurlwL0Pr2JWqBlQwzBjMbtLqlPk_Q" -X DELETE http://localhost/favorites/520ef1fd-7462-4fb9-9522-5c9c7af9d7e0/

