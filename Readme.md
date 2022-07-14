### Workflow
 - ręczne utworzenie migracji
  - 

### Alembic

Auto generowanie modelu
```bash
alembic revision --autogenerate -m "Add description"
```

Ręczne utworzenie migracji

```bash
alembic revision -m "Add manual change"
```



Uruchomienie wszystkich migracji:

```bash
alembic upgrade head
```

Rollback migracji 
```bash
alembic downgrade -1
```

### Postgres

```sql
CREATE TABLE shared.shared_users (
    id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    email varchar(256) UNIQUE NOT NULL,  
    tenant_id int NOT NULL,
	is_active bool NOT NULL DEFAULT false,
    created_at timestamptz NOT NULL DEFAULT timezone('utc', now()),
    updated_at timestamptz
);
```



```sql
CREATE TABLE tenant_default.users (
    id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    email varchar(256) UNIQUE,  
    first_name varchar(100),
    last_name varchar(100),
    user_role_id int,
    created_at timestamptz,
    updated_at timestamptz
);

CREATE TABLE tenant_default.permissions (
    id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    uuid uuid UNIQUE,
    account_id int,
    name varchar(100),
    title varchar(100),
    description varchar(100)
);


CREATE TABLE tenant_default.roles (
    id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    role_name varchar(100),
    role_description varchar(100)
);

CREATE TABLE tenant_default.roles_permissions_link (
    role_id int,
    permission_id int,
    PRIMARY KEY(role_id, permission_id)
);

ALTER TABLE tenant_default.roles_permissions_link ADD CONSTRAINT roles_permissions_link_fk FOREIGN KEY (permission_id) REFERENCES tenant_default.permissions(id);
ALTER TABLE tenant_default.roles_permissions_link ADD CONSTRAINT roles_permissions_link_fk_1 FOREIGN KEY (role_id) REFERENCES tenant_default.roles(id);
ALTER TABLE tenant_default.users ADD CONSTRAINT role_FK FOREIGN KEY (user_role_id) REFERENCES tenant_default.roles(id);
```

