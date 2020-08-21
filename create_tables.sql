

CREATE TABLE Client(
    ClientId        SERIAL,
    ClientFirstName VARCHAR,
    ClientLastName  VARCHAR,
    ClientDob       INT,
    Occupation      VARCHAR,
    PRIMARY KEY(ClientId)
);

CREATE TABLE Author(
    AuthorId          SERIAL,
    AuthorFirstName   VARCHAR,
    AuthorLastName    VARCHAR,
    AuthorNationality VARCHAR,
    PRIMARY KEY(AuthorId)
);

CREATE TABLE Book(
    BookId     SERIAL,
    BookTitle  VARCHAR,
    BookAuthor INT REFERENCES Author(AuthorId),
    Genre      VARCHAR,
    PRIMARY KEY(BookId)
);

CREATE TABLE Borrower(
    BorrowId   SERIAL,
    ClientId   INT REFERENCES Client(ClientId),
    BookId     INT REFERENCES Book(BookId),
    BorrowDate DATE,
    PRIMARY KEY(BorrowId)
);
