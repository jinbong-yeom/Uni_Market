package com.example.unimarket;

import java.util.List;

public class FilteringData {

    private List<String> excludeKeyword;

    private int maxPrice;

    private int minPrice;

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
