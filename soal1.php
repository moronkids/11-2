<?php
/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
$cek = array(
            "status"=>1,
            "message"=>"Data Found",
            "data"=>array(
              "name"=>"Sulistyo Ardani",
              "age"=>23,
              "address"=>"Jln.Ngawonggo Gg.Sadewa No.171 Ponowaren, Nogotirto, Gamping, Sleman, Yogyakarta",
              "hobbies"=>array(
                "motoran",
                "menggambar"
              ),
              "is_married"=>False,
              "list_school"=>array(
                ["name"=>"TK Tunas Mekar",
                "year_out"=>2003,
                "major"=>null],
                ["name"=>"SDN Nogotirto",
                "year_out"=>2008,
                "major"=>null,],
                ["name"=>"SMP N 3 Godean",
                "year_out"=>2011,
                "major"=>null,],
                ["name"=>"SMK N 3 Yogyakarta",
                "year_out"=>2014,
                "major"=>null,]
              ),
              "interest_in_coding"=>True
            )
          );
        $json = json_encode($cek);
        echo $json;
