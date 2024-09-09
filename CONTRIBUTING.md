# 🤝 Contributing

---

**Do NOT update the `README.md` file. It is updated from the [`/data`](https://github.com/wdhdev/free-for-life/tree/main/data) folder automatically.**

# 💻 Services

## 🚫 Disallowed Services
- 18+ services
- Illegal services
- Self hosted services
- Unfinished services
- Free subdomain providers that are not listed on the [Public Suffix List](https://publicsuffix.org)

## ✏️ Adding Services
1. Check if the service is already on the list.
2. Make sure your service is not a [disallowed service](#-disallowed-services).
3. Go to the [`/data`](https://github.com/wdhdev/free-for-life/tree/main/data) folder and click on the category the service matches and add it.
    - Make sure it is in the proper format.
        - e.g. `| [Service](https://example.com) | Description of the service. |`
    - Make sure it is in the correct category.
    - Make sure it is in alphabetical order.
    - Make sure the URL has no trailing slash.
        - ❌ `https://google.com/`
        - ✅ `https://google.com`
4. Open a pull request.
5. Wait for your pull request to be approved.

## 🗑️ Removing Services
1. Go to the [`/data`](https://github.com/wdhdev/free-for-life/tree/main/data) folder and click on the category the service is in.
2. Remove the service from the file.
3. Open a pull request.
4. Provide a reason in the description of your pull request for the removal of the service.
5. Wait for your pull request to be approved.

---

# 📖 Categories
## ✏️ Adding Categories
1. Create a file with the name of the category you want to add.
    - e.g. `APIs_Data_and_ML.md`
2. Adding a heading to the file with the category name.
    - e.g. `# APIs, Data and ML`
3. Create a table for the services.

```
| Website | Description |
|:-:|-|
```

4. Add at least one service to the table.
5. Add the category to the [Table of Contents](https://github.com/wdhdev/free-for-life/blob/main/data/_start.md).
6. Open a pull request.
7. Provide a reason in the description of your pull request for the adding of the category.
8. Wait for your pull request to be approved.

---

# 📜 Scripts
## 📝 Editing Scripts
1. Test that the updated script works in a [fork](https://github.com/wdhdev/free-for-life/fork) of this repository.
2. Open a pull request.
3. Provide a reason in the description of your pull request with the specified changes.
4. Wait for your pull request to be approved.
