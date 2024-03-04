package com.example.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.entity.dto.Account;
import org.apache.ibatis.annotations.Mapper;

// MyBatis-Plus 提供的通用 Mapper 接口。通用 Mapper 接口无需手动编写方法，它会根据实体类 Account 的字段自动生成常见的增删改查方法。
@Mapper
public interface AccountMapper extends BaseMapper<Account> {
}
