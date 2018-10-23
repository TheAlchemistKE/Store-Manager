[![Build Status](https://travis-ci.com/KelynPNjeri/Store-Manager.svg?branch=ft-get-specific-record-161330910)](https://travis-ci.com/KelynPNjeri/Store-Manager)
[![Coverage Status](https://coveralls.io/repos/github/KelynPNjeri/Store-Manager/badge.svg?branch=ft-get-specific-record-161330910)](https://coveralls.io/github/KelynPNjeri/Store-Manager?branch=ft-get-specific-record-161330910)
[![Maintainability](https://api.codeclimate.com/v1/badges/e61d01314f80973dd647/maintainability)](https://codeclimate.com/github/KelynPNjeri/Store-Manager/maintainability)
# Store-Manager API
These endpoints allow a user to perform a variety of functions clearly illustratrated in the table below such as displaying all the products in the inventory among other functions. 

### API ENDPOINTS
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/81faa37c129dadfd7c74)


<table class="tg">
  <tr>
    <th class="methods"><b>Methods</b></th>
    <th class="endpoints"><b>EndPoints</b></th>
    <th class="descriptions"><b>Descriptions</b></th>
  </tr>
  <tr>
    <td class="row1">GET</td>
    <td class="row1">'api/v1/products'</td>
    <td class="row1">Displays All Products.</td>
  </tr>
  <tr>
    <td class="row2">GET</td>
    <td class="row2">'api/v1/sales'</td>
    <td class="row2">Displays all Sales Records.</td>
  </tr>
  <tr>
    <td class="row3">POST</td>
    <td class="row3">'api/v1/sales'</td>
    <td class="row3">Allows creation of a new Sales Record.</td>
  </tr>
  <tr>
    <td class="row4">POST</td>
    <td class="row4">'api/v1/products'</td>
    <td class="row4">Allows creation of a new Product.</td>
  </tr>
  <tr>
    <td class="row5">GET</td>
    <td class="row5">'api/v1/products/productsId'</td>
    <td class="row5">Displays a Specific Product.</td>
  </tr>
  <tr>
    <td class="row6">GET</td>
    <td class="row6">'api/v1/salesId'</td>
    <td class="row6">Displays a Specific Sales Record.</td>
  </tr>
  <tr>
    <td class="row7">POST</td>
    <td class="row7">'api/v1/register'</td>
    <td class="row7">Registration of a new User.</td>
  </tr>
  <tr>
    <td class="row8">POST</td>
    <td class="row8">'api/v1/login'</td>
    <td class="row8">Allows Registered User to Login.</td>
  </tr>
</table>

### Documentation
[PostMan Docs](https://documenter.getpostman.com/view/5078064/RWgwSGUG)

## Deployment.
The API is currently deployed on Heroku.
[Heroku App](https://store-manager-kelyn-paul.herokuapp.com/)

## Authors
Kelyn Paul Njeri.

## Credits
This is part of the Andela Developer Challenge(ADC).



