package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

public class PostResponseData {

    @SerializedName("title")
    private String title;

    @SerializedName("picture")
    private String picture;

    @SerializedName("region")
    private String region;

    @SerializedName("price")
    private int price;

    @SerializedName("link")
    private String link;

    @SerializedName("app_name")
    private String app_name;

    @SerializedName("description")
    private String description;

    @SerializedName("date")
    private String date;

    @SerializedName("seller_info")
    private String seller_info;

    public String getTitle() {
        return title;
    }

    public String getPicture() {
        return picture;
    }

    public String getRegion() {
        return region;
    }

    public int getPrice() {
        return price;
    }

    public String getLink() {
        return link;
    }

    public String getApp_name() {
        return app_name;
    }

    public String getDescription() {
        return description;
    }

    public String getDate() {
        return date;
    }

    public String getSeller_info() {
        return seller_info;
    }

    public PostResponseData(String title, String picture, String region, int price, String link, String app_name, String description, String date, String seller_info) {
        this.title = title;
        this.picture = picture;
        this.region = region;
        this.price = price;
        this.link = link;
        this.app_name = app_name;
        this.description = description;
        this.date = date;
        this.seller_info = seller_info;
    }
}
