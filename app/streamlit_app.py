import streamlit as st
from compare_settings import compare_ini_settings
import datetime
import io

def main():
    st.title("INI File Comparison Tool")

    st.sidebar.header("Upload INI Files")
    file1 = st.sidebar.file_uploader("Choose the first INI file", type=["ini"])
    file2 = st.sidebar.file_uploader("Choose the second INI file", type=["ini"])

    if st.sidebar.button("Compare"):
        if file1 is not None and file2 is not None:
            content1 = file1.read().decode("utf-8")
            content2 = file2.read().decode("utf-8")

            changed_settings, added_settings, removed_settings = compare_ini_settings(content1, content2)

            def display_section(title, settings, color):
                st.markdown(f"<h3 style='color:{color};'>{title}</h3>", unsafe_allow_html=True)
                for section, items in settings.items():
                    st.markdown(f"<h4>{section}</h4>", unsafe_allow_html=True)
                    for key, value in items.items():
                        if isinstance(value, tuple):
                            old_val, new_val = value
                            st.markdown(f"<p style='color:{color}; white-space: nowrap;'>{key}: {old_val} → {new_val}</p>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<p style='color:{color}; white-space: nowrap;'>{key} = {value}</p>", unsafe_allow_html=True)

            if changed_settings:
                display_section("Changed Settings", changed_settings, "orange")

            if added_settings:
                display_section("Added Settings", added_settings, "green")

            if removed_settings:
                display_section("Removed Settings", removed_settings, "red")

            if not (changed_settings or added_settings or removed_settings):
                st.write("No differences found between the files.")

            log_content = "Changed Settings:\n"
            for section, changes in changed_settings.items():
                log_content += f"{section}:\n"
                for key, (old_val, new_val) in changes.items():
                    log_content += f"{key}: {old_val} → {new_val}\n"

            log_content += "\nAdded Settings:\n"
            for section, items in added_settings.items():
                log_content += f"{section}:\n"
                for key, value in items.items():
                    log_content += f"{key} = {value}\n"

            log_content += "\nRemoved Settings:\n"
            for section, items in removed_settings.items():
                log_content += f"{section}:\n"
                for key, value in items.items():
                    log_content += f"{key} = {value}\n"

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = f"comparison_log_{timestamp}.txt"

            st.sidebar.download_button(
                label="Save Log",
                data=log_content,
                file_name=log_filename,
                mime="text/plain"
            )

if __name__ == "__main__":
    main()