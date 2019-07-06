<?php
/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

function email($email)
{
    if(preg_match("/^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/", $email))
    {
        return "email valid";
    }
    else
    {
        return "email tidak valid";
    }
}
echo email('iqbal@mail.c');
echo "/ ";
function phone($phone)
{
    if(preg_match("/[+62][0-9]{8,15}$/", $phone))
    {
        return "phone valid";
    }
    else
    {
        return "phone tidak valid";
    }
}
echo phone('+628145789789789');
echo "/ ";
function username($username)
{
    if(preg_match("/[a-z]{5,9}$/", $username))
    {
        return "username valid";
    }
    else
    {
        return "username tidak valid";
    }
}
echo username('userOke');
echo "/ ";
// merupakan kombinasi dari huruf kecil, huruf besar, angka, dan
// karakter spesial minimal satu simbol dan harus terdapat simbol
// “#”. Dengan panjang minimal 8 karakter.

function password($password)
{
    $whiteListed = "\$\@\#\^\|\!\~\=\+\-\_\.";
    if(preg_match("/^[#a-zA-Z0-9\$\@\^\|\!\~\=\+\-\_\.]{8,}$/", $password))
    {
        if(preg_match_all("/[#]/", $password))
        {
        return "password valid";
        }
        else
        {
        return "password tidak valid";
        }
    }
    else
    {
        return "password tidak valid";
    }
}
echo password("C0d3YourFuture!@");
