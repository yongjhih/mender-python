#!/usr/bin/env bash

declare -A menders=(
    ["inventory"]="https://raw.githubusercontent.com/mendersoftware/inventory/master/docs/management_api.yml"
    ["useradm"]="https://raw.githubusercontent.com/mendersoftware/useradm/master/docs/management_api.yml"
    ["deviceadm"]="https://raw.githubusercontent.com/mendersoftware/deviceadm/master/docs/management_api.yml"
    ["deployments"]="https://raw.githubusercontent.com/mendersoftware/deployments/master/docs/management_api.yml"
    ["deviceauth"]="https://raw.githubusercontent.com/mendersoftware/deviceauth/master/docs/management_api.yml"
)

for mender in "${!menders[@]}"; do
    url="${menders[$mender]}"
    mkdir -p "docs/$mender"
cat > "docs/$mender/index.html" <<EOF
<!DOCTYPE html>
<html>
  <head>
    <title>ReDoc</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">

    <!--
    ReDoc doesn't change outer page styles
    -->
    <style>
      body {
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <redoc spec-url='$url'></redoc>
    <script src="//cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"> </script>
  </body>
</html>
EOF
done
