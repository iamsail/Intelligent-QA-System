<?php
/**
 * Created by PhpStorm.
 * User: sail
 * Date: 18-6-25
 * Time: 上午12:48
 */

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;
class AppController
{

    /**
     * 获取所有QA对
     *
     * @return {array}　$arr  QA对
     */
    public function getQA() {
        $arr = array();
        $arr['QA'] = DB::select('select * from all_QA');
        return $arr;
    }

    /**
     * 用户登录
     *　
     * @param  {Request} $request 用于请求
     * @return {number}　$final  状态码　0 用户不存在; 1　登录成功; 2　密码错误;
     */
    public function login(Request $request) {
        $input = $request->all();
        $result = DB::select('select * from admin where username = ?', [$input['username']]);
        $final = null;
        if ($result == null) {
            $final = 0;
        } elseif ($result[0] -> password == $input['password']) {
            session(['username' => $input['username']]);
            $final  = 1;
        } else {
            $final  = 2;
        }
        return $final;
    }
}