package com.example.unimarket;

import android.app.Application;

public class Globalstr extends  Application {
    private String region1;
//    private String region2;
//    private String region3;

    public String getregion1() {return region1;}
//    public String getregion2() {return region2;}
//    public String getregion3() {return region3;}


    public void setregion1( String input ) { this.region1 = input; }

    public Globalstr(){
        this.region1 = "";
//        this.region2 = "";
//        this.region3 = "";
    }
}
