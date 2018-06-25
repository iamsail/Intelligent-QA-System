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
        return $arr;
    }


    public function getQA() {
        $arr = array();
        $arr['QA'] = DB::select('select * from all_QA');
        return $arr;
    }
}