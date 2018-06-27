<!doctype html>
<html lang="{{ app()->getLocale() }}">
     <head>
             <meta charset="utf-8">
             <meta http-equiv="X-UA-Compatible" content="IE=edge">
             <meta name="viewport" content="width=device-width, initial-scale=1">
             <meta name="csrf-token" content="{{ csrf_token() }}">

             <title>智能对话系统</title>
             <link href="https://cdn.bootcss.com/minireset.css/0.0.2/minireset.min.css" rel="stylesheet">
             <style>
                html {
                    width: 100vw;
                    height: 100vh;
                    background: #BAF2E8;
                }
             </style>

             <!-- Fonts -->
             <link href="https://fonts.googleapis.com/css?family=Raleway:100,600" rel="stylesheet" type="text/css">
             <style>
                 * {
                     font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
                 }
             </style>

         </head>
     <body>
         <div id="app">
         </div>
     </body>
     <script src="/js/qa.js"></script>
</html>