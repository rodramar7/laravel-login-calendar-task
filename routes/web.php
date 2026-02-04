<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Caller\LoginController;

Route::get('/', [LoginController::class, 'index']);
Route::get('/login', [LoginController::class, 'index'])->name('login');
Route::post('/login', [LoginController::class, 'validateUser']);
Route::get('/login/{driver}/start', [LoginController::class, 'redirectToProvider']);
Route::any('/login/{driver}/callback', [LoginController::class, 'handleProviderCallback']);
Route::any('/logout', [LoginController::class, 'Logout']);
Route::get('/html-page', function () {
    return view('calender');
});
