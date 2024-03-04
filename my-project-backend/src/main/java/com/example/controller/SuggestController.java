package com.example.controller;

import com.example.entity.RestBean;
import com.example.entity.vo.response.SuggestVO;
import com.example.service.SuggestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/suggest")
public class SuggestController {

    @Autowired
    private SuggestService suggestService;

    @GetMapping("/{category}")
    public RestBean<SuggestVO> getSuggest(@PathVariable String category) {
        SuggestVO suggest = suggestService.fetchSuggest(category);
        return (suggest != null) ? RestBean.success(suggest) : RestBean.failure(404, "Suggest not found");
    }

    @GetMapping("/all")
    public RestBean<List<SuggestVO>> getAllSuggestions() {
        List<SuggestVO> suggestions = suggestService.fetchAllSuggestions();
        return (suggestions != null && !suggestions.isEmpty()) ?
                RestBean.success(suggestions) : RestBean.failure(404, "No suggestions found");
    }
}
