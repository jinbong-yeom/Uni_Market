package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

public class PostData {
    @SerializedName("title")
    private String title;

    @SerializedName("userId")
    private String userId;

    public String getTitle() {
        return title;
    }

    public String getUserId() {
        return userId;
    }

    public PostData(String title, String userId) {
        this.title = title;
        this.userId = userId;
    }
}
