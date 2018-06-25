<!doctype html>
<html lang="{{ app()->getLocale() }}">
     <head>
             <meta charset="utf-8">
             <meta http-equiv="X-UA-Compatible" content="IE=edge">
             <meta name="viewport" content="width=device-width, initial-scale=1">
             <meta name="csrf-token" content="{{ csrf_token() }}">

             <title>智能对话系统</title>

             <!-- Fonts -->
             <link href="https://fonts.googleapis.com/css?family=Raleway:100,600" rel="stylesheet" type="text/css">

         </head>
     <body>
         <div id="app">
         </div>
     </body>
     <script src="/js/app.js"></script>
</html>