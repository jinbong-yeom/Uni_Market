package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

public class DeleteData {

    @SerializedName("userId")
    private String userId;

    public DeleteData(String userId) {
        this.userId = userId;
    }

    public String getUserId() {
        return userId;
    }
}
