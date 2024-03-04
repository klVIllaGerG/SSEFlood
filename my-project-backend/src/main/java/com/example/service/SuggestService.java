package com.example.service;

import com.example.entity.vo.response.SuggestVO;

import java.util.List;

public interface SuggestService {
    SuggestVO fetchSuggest(String category);
    List<SuggestVO> fetchAllSuggestions(); // 如果需要获取所有建议
}