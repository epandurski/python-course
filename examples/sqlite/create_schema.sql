CREATE TABLE IF NOT EXISTS expenses
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    date TEXT NOT NULL,
    description NVARCHAR(200) NOT NULL,
    amount Numeric NOT NULL
);

CREATE INDEX ix_expenses_data ON expenses (date);
