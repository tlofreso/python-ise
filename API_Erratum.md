# Cisco ISE ERS API Erratum

This file records any errors within Cisco's API documentaion I may have come across while writing python-ise. The documentaion I'm referencing may be found on any ISE server at: `https://<ise_endpoint>:9060/ers/sdk`

### ANC Endpoint Operations

#### Clear operaion has wrong URL listed
Location: `https://<ise_endpoint>:9060/ers/sdk > API Documentaion > ANC Endpoint > clear`

URL is listed as: `.../ers/config/ancendpoint/apply`
URL should be: `.../ers/config/ancendpoint/clear`

#### `ipAddress` is not a valid additional attribute
Location: `https://<ise_endpoint>:9060/ers/sdk > API Documentaion > ANC Endpoint > clear`
Location: `https://<ise_endpoint>:9060/ers/sdk > API Documentaion > ANC Endpoint > apply`

Both locations likst ipAddress as a valid additional attribute, but this is not true. ANC Endpoints appear to only support macAddress.