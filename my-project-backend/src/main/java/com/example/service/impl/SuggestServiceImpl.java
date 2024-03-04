package com.example.service.impl;

import com.example.entity.vo.response.SuggestVO;
import com.example.service.SuggestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SuggestServiceImpl implements SuggestService {

    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public SuggestServiceImpl(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Override
    public SuggestVO fetchSuggest(String category) {
        // 使用 JdbcTemplate 执行数据库查询操作
        String sql = "SELECT category, suggestions FROM suggestion WHERE category = ?";
        return jdbcTemplate.queryForObject(sql, new Object[]{category}, (resultSet, i) -> {
            SuggestVO suggestVO = new SuggestVO();
            suggestVO.setCategory(resultSet.getString("category"));
            suggestVO.setSuggestions(resultSet.getString("suggestions"));
            return suggestVO;
        });
    }

    public List<SuggestVO> fetchAllSuggestions() {
        // 实现获取所有建议的逻辑，可以使用类似的 JdbcTemplate 查询
        // 请根据你的数据库结构和需求进行相应的修改
        String sql = "SELECT category, suggestions FROM suggestion";
        return jdbcTemplate.query(sql, (resultSet, i) -> {
            SuggestVO suggestVO = new SuggestVO();
            suggestVO.setCategory(resultSet.getString("category"));
            suggestVO.setSuggestions(resultSet.getString("suggestions"));
            return suggestVO;
        });
    }
}