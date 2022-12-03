package com.example.unimarket;

import java.util.List;

public class FilteringData {

    private List<String> excludeKeyword;

    private int maxPrice;

    private int minPrice;

    public FilteringData(List<String> excludeKeyword, int maxPrice, int minPrice) {
        this.excludeKeyword = excludeKeyword;
        this.maxPrice = maxPrice;
        this.minPrice = minPrice;
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
