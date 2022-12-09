package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

public class DeleteResponse {

    @SerializedName("result")
    private Boolean result;

    public DeleteResponse(Boolean result) {
        this.result = result;
    }

    public Boolean getResult() {
        return result;
    }
}
