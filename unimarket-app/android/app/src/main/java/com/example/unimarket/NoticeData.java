package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

public class NoticeData {
    @SerializedName("title")
    private String title;

    @SerializedName("userId")
    private String userId;

    @SerializedName("firebaseId")
    private String firebaseId;

    @SerializedName("filteringData")
    private FilteringData filteringData;

    @SerializedName("isSend")
    private Boolean send;



    public NoticeData(String title, String userId, String firebaseId, FilteringData filteringData, Boolean send) {
        this.title = title;
        this.userId = userId;
        this.firebaseId = firebaseId;
        this.filteringData = filteringData;
        this.send = send;
    }

    public String getFirebaseId() {
        return firebaseId;
    }

    public Boolean getSend() {
        return send;
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
