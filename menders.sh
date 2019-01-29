#!/usr/bin/env bash

menders=(
    ["inventory"]="https://github.com/mendersoftware/inventory/raw/master/docs/management_api.yml"
    ["useradm"]="https://github.com/mendersoftware/useradm/raw/master/docs/management_api.yml"
    ["deviceadm"]="https://github.com/mendersoftware/deviceadm/raw/master/docs/management_api.yml"
    ["deployments"]="https://github.com/mendersoftware/deployments/raw/master/docs/management_api.yml"
    ["deviceauth"]="https://github.com/mendersoftware/deviceauth/raw/master/docs/management_api.yml"
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
