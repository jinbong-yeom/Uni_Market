package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class PostData {
    @SerializedName("title")
    private String title;

    @SerializedName("userId")
    private String userId;

<<<<<<< HEAD
    @SerializedName("filteringData")
    public FilteringData filteringData;
=======
    @SerializedName("region")
    private List<String> region;

    public PostData(String title, String userId, List<String> region) {
        this.title = title;
        this.userId = userId;
        this.region = region;
    }
>>>>>>> Feature_Firebase_Test

    public String getTitle() {
        return title;
    }


    public String getUserId() {
        return userId;
    }

<<<<<<< HEAD
    public FilteringData getFilteringData() {
        return filteringData;
    }

    public PostData(String title, String userId, FilteringData filteringData) {
        this.title = title;
        this.userId = userId;
        this.filteringData = filteringData;
=======
    public List<String> getRegion() {
        return region;
>>>>>>> Feature_Firebase_Test
    }
}
