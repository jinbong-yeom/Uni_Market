package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class NoticeResponse {
    @SerializedName("result")
    private Boolean result;

    public NoticeResponse(Boolean result) {
        this.result = result;
    }

    public Boolean getResult() {
        return result;
    }
}
