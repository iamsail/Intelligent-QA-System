<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Http\RedirectResponse;

class LoginCheck
{
    /**
     * Handle an incoming request.
     * 如果用户尚未登录则跳转到登录界面
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {

        $value = $request->session()->get('username');
        if ($value == null) {
            return redirect('/login');
        }
        return $next($request);
    }
}
