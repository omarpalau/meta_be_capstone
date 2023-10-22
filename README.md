# META CAPSTONE README

Follow these steps to grade my project.

## Prerequisites:

Make sure to complete the following before any test:

1. Clone the repository: `https://github.com/omarpalau/meta_be_capstone.git`.
3. Make sure to execute the project in a dev environment `pipenv shell`.
4. Make sure to install the Pipfile dependencies `pipenv install`.
5. CD to my project's `./littlelemon/` directory.
6. Run the server `python3 manage.py runserver`.

Consider the following admin credentials:

<table>
  
  <tr>
    <th>
      username:  
    </th>
    <td>
      `root`
    </td>
  </tr>

  <tr>
    <th>
      password:  
    </th>
    <td>
      `root`
    </td>
  </tr>
  
</table>

## API Endpoints

Consider the following endpoints:

|Local URL|Project Endpoint|API Endpoint|
|-|-|-|
|127.0.0.1:8000/|[/admin/](http://127.0.0.1:8000/admin/)||
||<p>[/auth/](http://127.0.0.1:8000/auth/)</p><p>Consider the [djsoer documentation](https://djoser.readthedocs.io/en/latest/token_endpoints.html) for a full list of endpoints</p>||
||[/restaurant/](http://127.0.0.1:8000/restaurant/)|[/menu/](http://127.0.0.1:8000/restaurant/menu/)|
|||[/menu/{num}](http://127.0.0.1:8000/restaurant/menu/1) (...1,2,3)|
|||[/booking/](http://127.0.0.1:8000/restaurant/booking/)|
|||[/api-token-auth/](http://127.0.0.1:8000/restaurant/api-token-auth/)|


# Thank you!!!
