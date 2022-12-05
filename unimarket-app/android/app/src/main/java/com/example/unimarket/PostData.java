package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class PostData {
    @SerializedName("title")
    private String title;

    @SerializedName("userId")
    private String userId;

    @SerializedName("filteringData")
    private FilteringData filteringData;

    public PostData(String title, String userId, FilteringData filteringData) {
        this.title = title;
        this.userId = userId;
        this.filteringData = filteringData;
    }

    public String getTitle() {
        return title;
    }

    public String getUserId() {
        return userId;
    }

    public FilteringData getFilteringData() {
        return filteringData;
    }
}
