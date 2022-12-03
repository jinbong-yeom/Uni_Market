package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class PostData {
    @SerializedName("title")
    private String title;

    @SerializedName("userId")
    private String userId;

    @SerializedName("region")
    private List<String> region;

    public PostData(String title, String userId, List<String> region) {
        this.title = title;
        this.userId = userId;
        this.region = region;
    }

    public String getTitle() {
        return title;
    }

    public String getUserId() {
        return userId;
    }

    public List<String> getRegion() {
        return region;
    }
}
