<?php
/**
 * Created by PhpStorm.
 * User: sail
 * Date: 18-7-4
 * Time: 下午8:02
 */

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class FeController
{

    public function ask (Request $request) {
        $question = $request->all()['question'];
        $dir = getcwd();
        $dir = substr($dir, 0, strlen($dir ) - 9);
        unset($out);
        $c = exec("/usr/bin/python3.5 ".$dir."model/core/cal_text_similarity.py 2>&1 {$question}",$out,$res);
        return $out[sizeof($out) - 1];
    }
}