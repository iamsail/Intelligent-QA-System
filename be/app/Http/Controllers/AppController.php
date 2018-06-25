<?php
/**
 * Created by PhpStorm.
 * User: sail
 * Date: 18-6-25
 * Time: 上午12:48
 */

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;

class AppController
{
    public function test () {
        $arr = array();
        $arr['key'] = 'sail';
        $arr['db'] = DB::select('select * from all_QA where id = ?', [1]);;

        return $arr;
    }
}