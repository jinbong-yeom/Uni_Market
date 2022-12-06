package com.example.unimarket;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class FilteringData {

    @SerializedName("excludeKeyword")
    private List<String> excludeKeyword;

    @SerializedName("maxPrice")
    private int maxPrice;

    @SerializedName("minPrice")
    private int minPrice;

    @SerializedName("region")
    private List<String> region;

    public FilteringData(List<String> excludeKeyword, int maxPrice, int minPrice, List<String> region) {
        this.excludeKeyword = excludeKeyword;
        this.maxPrice = maxPrice;
        this.minPrice = minPrice;
        this.region = region;
    }

    public List<String> getRegion() {
        return region;
    }

    public List<String> getExcludeKeyword() {
        return excludeKeyword;
    }

    public int getMaxPrice() {
        return maxPrice;
    }

    public int getMinPrice() {
        return minPrice;
    }
}
